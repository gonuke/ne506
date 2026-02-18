# plotting helper functions
def plot_geom(x_c, R):
    """
    Start a 3-D plot and put the spherical surface and plane on the plot
    
    parameters
    -----------
    x_c : (numpy array of 3 floats) Coordinates of center of sphere
    R : (float) Radius of sphere

    returns
    ---------
    ax : axis object
    """
    
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(projection='3d')

    # calculate lattitude and longitude
    long, lat = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j] 

    # generate x,y,z points at all the lat/long combinations
    x = R * np.cos(long) * np.sin(lat) + x_c[0]
    y = R * np.sin(long) * np.sin(lat) + x_c[1]
    z = R * np.cos(lat) + x_c[2]

    # plot a translucent surface
    ax.plot_surface(x, y, z, linewidth=0, alpha=0.15, color="gray")
    ax.plot_surface(x_c[0], y, z, linewidth=1, alpha=0.15, color="purple")
    
    return ax

def plot_event(ax, event_type, x, print_event=False):
    """
    Plot a marker for an event where the color depends on the plot type.
    
    Optionally print the details of the event
    
    parameters
    -----------
    ax : axis object on which to add marker
    event_type : (str) event type
    x : (numpy array of 3 floats) Coordinates of current particle position
    """
    
    color = {"source" : "green", "collision" : "yellow", "plane" : "black", "sphere" : "red"}
    ax.plot(*x, color=color[event_type], marker="x")
    if print_event:
        print(event_type, x, u)

    
def plot_track(ax, x_old, x_new):
    """
    Plot a line indicating a particle track.
    
    parameters
    -----------
    x_old : (numpy array of 3 floats) Coordinates of the beginning of the track
    x_new : (numpy array of 3 floats) Coordinates of the end of the track

    """
    
    pts = np.concatenate([x_old, x_new]).reshape(2,3).T
    ax.plot(*pts, color="black")