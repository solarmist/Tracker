function show_graph(series, title) {
    $.jqplot.config.enablePlugins = true;
    // Invarients
    var xaxis = {renderer:$.jqplot.DateAxisRenderer,
                 pad: 0,
		 autoscale: true,
                 labelRenderer: $.jqplot.CanvasAxisLabelRenderer,
                 tickRenderer: $.jqplot.CanvasAxisTickRenderer,
                 numTicks: 15,
                 tickOptions: {angle:-30, formatString:'%v',
			      }
                };
    var axesDefaults = {useSeriesColor: true,
                        rendererOptions: {alignTicks: true}
                       };
    var options = {
        axesDefaults: axesDefaults,
        axes:{xaxis: xaxis
             },
        series: [],
        seriesDefault: {showMarker: true},
        title:title,
        legend:{show: true},
        animate: true,
        cursor: {show: true,
                 zoom: true}
    };
    var macroOptions = {
        axesDefaults: axesDefaults,
        axes:{xaxis:xaxis
             },
        series: [],
        seriesDefaults: {showMarker: false},
        animate: false,
        cursor: {show: true,
                 showTooltip: false,
                 constrainZoomTo: 'x',
                 zoom: true}
    };
    var style = $.jqplot.MovingAverageRenderer;

    // For each series we need a series_style and yaxis
    var data = [];
    for (var i=0; i<series.length; i++) {
        var title = series[i]['title'];
        var axis = 'y'+ ((i>0)?i+1:'') +'axis';
        options['series'].push({label: title, yaxis:axis,
                                renderer:style,
                                rendererOptions:{showMarker:true}});
        macroOptions['series'].push({label: title, yaxis:axis});

        options['axes'][axis] = {label: title + ' (' + series[i]['units'] + ')',
			autoscale: true,
			tickOptions: {formatString:'%.1f'},
			tickRenderer: $.jqplot.CanvasAxisTickRenderer,
			labelRenderer: $.jqplot.CanvasAxisLabelRenderer,
			rendererOptions:{}
                                };
        macroOptions['axes'][axis] = options['axes'][axis];
        data.push(series[i]['data']);
    }
    var targetPlot = $.jqplot("target", data, options);
    var controllerPlot = $.jqplot("controller", data, macroOptions);

    $.jqplot.Cursor.zoomProxy(targetPlot, controllerPlot);

    return [targetPlot, controllerPlot];

}

function jqplot_zoomDates(start, end, plot) {
    // Zoom to the last 'days' of the graph
    plot.axes.xaxis.reset();
    plot.axes.xaxis.resetScale();
    var min = Math.max(plot.axes.xaxis._min, start.getTime());
    var max = Math.min(plot.axes.xaxis._max, end.getTime());
    if (max > plot.axes.xaxis._max) {
        min -= max - plot.axes.xaxis._max;
        max = plot.axes.xaxis._max;
    }

    if (min < plot.axes.xaxis._min)
        min = plot.axes.xaxis._min;

    plot.axes.xaxis.min = min;
    plot.axes.xaxis.max = max;
    console.log(new Date(min));
    console.log(new Date(max));
    console.log(plot.axes.xaxis);
    plot.redraw();

} 