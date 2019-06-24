def get_nba_data(endpoint, params, return_url=False):
    
    """Retrieves data from http://stats.nba.com
    
    For community documentation, visit 
    https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation.
    
    Args:
        endpoint: endpoint specifies data table
        params: dictionary of parameters: e.g., {'LeagueID':'00'}
        return_url: returns URL instead of downloading data then returning it
    Returns:
        out: Pandas data frame
    """
    
    from pandas import DataFrame
    from urllib.parse import urlencode
    import json
    import subprocess as sp
    
    useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
    dataurl = "http://stats.nba.com/stats/" + endpoint + "?" + urlencode(params)
    
    # for debugging: just return the url
    if return_url:
        return(dataurl)
    
    wgetout = sp.Popen(['wget', '-q', '-O', '-', '--user-agent='+useragent, dataurl], stdout=sp.PIPE)
    
    jsonstr, _ = wgetout.communicate()
    data = json.loads(jsonstr)
    
    h = data['resultSets'][0]['headers']
    d = data['resultSets'][0]['rowSet']
    
    out = DataFrame(d, columns=h)
    
    return(out)


def bin_shots(df, bin_edges, density=False, sigma=1):
    
    """Given data frame of shots, a 2d matrix of binned counts is computed
    
    Args:
        df: data frame of shotchartdetail from nba.com. 
            At the minimum, LOCX and LOCY are required.
        bin_edges: bin edge definition: edges in x and edges in y
    
    Returns:
        binned: counts
        xedges: bin edges in X direction
        yedges: bin edges in Y direction
    """
    import numpy as np
    from scipy import ndimage
    
    binned, xedges, yedges = np.histogram2d(df.LOC_X, df.LOC_Y, bins=bin_edges)
    
    if density:
        binned = ndimage.filters.gaussian_filter(binned, sigma)
        binned /= np.sum(binned)
    
    return(binned, xedges, yedges)


def draw_court(ax=None, color='black', lw=1, outer_lines=False):
    
    """Draws a half basketball court
    This function is from http://savvastjortjoglou.com/nba-shot-sharts.html
    
    Args:
        ax: figure axes [None]
        color: ['black']
        lw: linewidth [1]
        outer_lines: court perimeter [False]
        
    Returns:
        ax: figure axes with court
    """
    
    from matplotlib.patches import Circle, Rectangle, Arc
    from matplotlib.pyplot import gca
    
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = gca()

    # Create the various parts of an NBA basketball court

    # Create the basketball hoop
    # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # 7.5 in our coordinate system
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    # Create backboard
    backboard = Rectangle((-30, -7.5), 60, 0, linewidth=lw, color=color)

    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                          fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                          fill=False)

    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-219, -47.5), 0, 140, linewidth=lw,
                               color=color)
    corner_three_b = Rectangle((219, -47.5), 0, 140, linewidth=lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the 
    # threes
    three_arc = Arc((0, 0), 475, 475, theta1=22.5, theta2=157.5, linewidth=lw,
                    color=color)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                           linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                           linewidth=lw, color=color)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax


def plot_shotchart(hist_counts, xedges, yedges, ax=None, use_log=False):
    
    """Plots 2d heatmap from vectorized heatmap counts
    
    Args:
        hist_counts: vectorized output of numpy.histogram2d
        xedges, yedges: bin edges in arrays
        ax: figure axes [None]
        use_log: will convert count x to log(x+1) to increase visibility [False]
    Returns:
        ax: axes with plot
    """
    
    import numpy as np
    import matplotlib.pyplot as plt
    import helper_basketball as h
    
    nx = xedges.size - 1
    ny = yedges.size - 1
    
    counts = hist_counts.reshape((nx, ny))
    
    X, Y = np.meshgrid(xedges, yedges)
    
    if use_log:
        counts = np.log(counts + 1)
        
    if ax is None:
        fig, ax = plt.subplots(1,1)
    
    ax.pcolormesh(X, Y, counts.T, cmap='jet', vmin=0., vmax=0.005)
    ax.set_aspect('equal')
    
    draw_court(ax)
    
    return(ax)
