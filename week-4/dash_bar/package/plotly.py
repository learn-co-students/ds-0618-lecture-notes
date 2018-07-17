def trace_values(x_values, y_values, mode = None, name="data", text = [], type='scatter',options = {}):
    trace = {'x': x_values, 'y': y_values, 'name': name, 'text': text, 'type': type}
    if mode:
        mode.update({'mode': mode})
    trace.update(options)
    return trace

def build_layout(x_axis = None, y_axis = None, options = {}):
    layout = {}
    if isinstance(x_axis, dict): layout.update({'xaxis': x_axis})
    if isinstance(y_axis, dict): layout.update({'yaxis': y_axis})
    layout.update(options)
    return layout
