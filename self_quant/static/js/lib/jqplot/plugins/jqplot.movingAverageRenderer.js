/**
 * jqPlot.movingAverageRenderer
 * Pure JavaScript plotting plugin using jQuery
 *
 * Copyright (c) 2009-2012 Joshua Olson
 * jqPlot is currently available for use in all personal or commercial projects 
 * under both the MIT (http://www.opensource.org/licenses/mit-license.php) and GPL 
 * version 2.0 (http://www.gnu.org/licenses/gpl-2.0.html) licenses. This means that you can 
 * choose the license that best suits your project and use it accordingly. 
 *
 *
 * sprintf functions contained in jqplot.sprintf.js by Ash Searle:
 *
 *     version 2007.04.27
 *     author Ash Searle
 *     http://hexmen.com/blog/2007/03/printf-sprintf/
 *     http://hexmen.com/js/sprintf.js
 *     The author (Ash Searle) has placed this code in the public domain:
 *     "This code is unrestricted: you are free to use it however you like."
 * 
 */
(function($) {
     /**
      * Class: $.jqplot.MovingAverageRenderer
      * jqPlot Plugin to draw moving averages with deviations
      * 
      * To use this plugin, include the renderer js file in 
      * your source:
      * 
      * > <script type="text/javascript" src="plugins/jqplot.movingAverageRenderer.js"></script>
      * 
      * You will most likely want to use a date axis renderer
      * for the x axis also, so include the date axis render js file also:
      * 
      * > <script type="text/javascript" src="plugins/jqplot.dateAxisRenderer.js"></script>
      * 
      * Then you set the renderer in the series options on your plot:
      * 
      * > series: [{renderer:$.jqplot.movingAverageRenderer}]
      * 
      * > dat = [['07/06/2009',138.7], ['06/29/2009',143.46], ...]
      * 
      */
     $.jqplot.MovingAverageRenderer = function(){
         // subclass line renderer to make use of some of it's methods.
         $.jqplot.LineRenderer.call(this);
         // prop: N
         // Days in moving average
         // Default is 10.
         this.N = 10;	 
         // prop: lineColor
         // color of the moving average line
         // Default is the series color.
         this.lineColor = null;
         // prop: wickUpColor
         // color of the wick when trending up
         // Default is the series color.
         this.wickUpColor = '#FF0000';
         // prop: wickDownColor
         // color of the wick when trending down
         // Default is the series color.
         this.wickDownColor = '#000000';
         // prop: lineWidth
         // Width of the hi-low line and open/close ticks.
         // Must be set in the rendererOptions for the series.
         this.lineWidth = 2.0;
     };
     
     $.jqplot.MovingAverageRenderer.prototype = new $.jqplot.LineRenderer();
     $.jqplot.MovingAverageRenderer.prototype.constructor = $.jqplot.MovingAverageRenderer;
     
     // called with scope of series.
     $.jqplot.MovingAverageRenderer.prototype.init = function(options) {
         options = options || {};
         // lineWidth and N have to be set on the series, changes in renderer
         // constructor have no effect.  set the default here
         // if no renderer option for lineWidth is specified.
         this.lineWidth = options.lineWidth || 2.0;
	 this.N = options.N || 10;
         $.jqplot.LineRenderer.prototype.init.call(this, options);
         this._type = 'movingaverage';
         // set the yaxis data bounds here to account for hi and low values
         var db = this._yaxis._dataBounds;
         var d = this._plotData;

     };
     // Calculate the moving average for the points
     // This will be a plugable function
     $.jqplot.MovingAverageRenderer.prototype.expMovingAverage = function (d, N) {
	 //TODO: How do I get access to N?
	 var N = N||10;
	 var a = 2 / (N + 1);
	 d[0][2] = d[0][1];
	 for (var i=1; i<d.length; i++) {
	     d[i][2] = a * d[i][1] + (1-a) * d[i-1][2];
	 }
     };

     // called within scope of series
     // Add our moving average points to the griddata before calling makeGridData
     $.jqplot.MovingAverageRenderer.prototype.makeGridData = function(data, plot) {
	 // Get the days for the moving average
         var xp = this._xaxis.series_u2p;
         var yp = this._yaxis.series_u2p;
         var xmin = this._xaxis.min;
         var xmax = this._xaxis.max;
         // index of last value below range of plot.
         var xminidx = 0;
	 $.jqplot.MovingAverageRenderer.prototype.expMovingAverage(data, this.N);
         for (var i=0; i<data.length; i++) {
             if (data[i][0] < xmin) {
                 xminidx = i;
             }
             else if (data[i][0] < xmax) {
                 xmaxidx = i + 1;
             }
         }
         var xmaxidx = data.length;
	 var gd = [];
         for (i=xminidx; i<xmaxidx; i++) {
             var x1 = xp(data[i][0]);
	     var yd = yp(data[i][1]);
             var y1 = yp(data[i][2]);
	     gd.push([x1,y1,yd]);
	     gd.push([x1,yd]);
	 }

    	 return gd;
     };

     // called within scope of series.
     $.jqplot.MovingAverageRenderer.prototype.draw = function(ctx, gd, options) {
         var d = this.data;
         var prevColor, prevMarkerOptions, ops;
         var r = this.renderer;
         var opts = (options != undefined) ? options : {};
         var shadow = (opts.shadow != undefined) ? opts.shadow : this.shadow;
         var fill = (opts.fill != undefined) ? opts.fill : this.fill;
         var fillAndStroke = (opts.fillAndStroke != undefined) ? opts.fillAndStroke : this.fillAndStroke;
	 var shadow_gd = [];

         ctx.save();
         if (this.show) {
             var x1, x2, y1, y2, yd, i;
             for (i=0; i<gd.length - 1; i+=2) {
		 var x1 = gd[i][0];
		 var y1 = gd[i][1];
		 var yd = gd[i][2];
		 if (i< gd.length - 2) {
		     var x2 = gd[i+2][0];
		     var y2 = gd[i+2][1];
		 }
		 shadow_gd.push([x1,y1]);
                 // draw wick
		 prevColor = opts.color;

		 // yd and y1 are in screen coordinates so yd < y1 means the wick is going up		
                 if (yd < y1 && r.wickUpColor) {
                     opts.color = r.wickUpColor;
                 }
		 else if (r.wickDownColor) {
		     opts.color = r.wickDownColor;
		 }
                 r.shapeRenderer.draw(ctx, [[x1, y1], [x1, yd]], opts);
		 opts.color = prevColor;

		 // draw line to the next point if we have a next point
		 if (i < gd.length) {
		     prevColor = opts.color;
		     if (r.lineColor) {
			 opts.color = r.lineColor;
		     }
		     r.shapeRenderer.draw(ctx, [[x1, y1], [x2, y2]], opts);
                     opts.color = prevColor;

		 }
                 if (this.markerRenderer.show) {
		     //Optional different color markers
                     this.markerRenderer.draw(x1, yd, ctx, opts.markerOptions);
                 }

             }
             if (shadow) {
                 this.renderer.shadowRenderer.draw(ctx, shadow_gd, opts);
             }

         }
         
         ctx.restore();
     };  
     
     $.jqplot.MovingAverageRenderer.prototype.drawShadow = function(ctx, gd, options) {
         // This is a no-op, shadows drawn with lines.
     };
     
     // called with scope of plot.
     $.jqplot.MovingAverageRenderer.checkOptions = function(target, data, options) {
         // provide some sensible highlighter options by default

         if (!options.highlighter) {
             options.highlighter = {
                 showMarker:false,
		 tooltipFormatString: 'Label?%.1F',
                 tooltipAxes: 'y'
             };
         }
     };
     
     $.jqplot.preInitHooks.push($.jqplot.MovingAverageRenderer.checkOptions);
     
 })(jQuery);    