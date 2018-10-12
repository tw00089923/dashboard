var setting = { displayModeBar: false ,scrollZoom: false,editable: false , responsive: true};


function drawline(x,y,div){
    var data = [{
        x: x,
        y: y,
        type: 'scatter',
        marker: { line: {color:'rgb(55, 128, 1)',width:1} },
        line: {color: 'white',width:1}
        }];
    
      var width = 120,height=120;
      var d3 = Plotly.d3;   
      var gd3 = d3.select(div)
            .append("div")
            .style({height:height+"px" })
      var gd = gd3.node()
      var layout = {
        hovermode: false,
        autosize:true,
        xaxis: {
        autorange: true,
        showgrid: false,
        zeroline: false,
        showline: false,
        autotick: true,
        fixedrange : true,
        ticks: '',
        showticklabels: false
      },
      yaxis: {
        autorange: true,
        range:[1,8],
        showgrid: false,
        zeroline: false,
        showline: false,
        autotick: true,
        fixedrange : true,
        ticks: '',
        showticklabels: false
      },
      margin:{
        l:0,r:0,b:10,t:10,pad:10
      },
      plot_bgcolor:"#343a40",
      height:height
    };
    
   
    return  Plotly.newPlot(gd, data, layout, setting );
  

}

function piechart(x,y,div,width,showlegend=true){
    var height = 200;
    var width = width;
    var d3 = Plotly.d3;   
    var gd3 = d3.select(div)
          .append("div")
          .style({height:height+"px" })
    var gd = gd3.node()
    var data = [{
        values: x,  //[19, 26, 55]
        labels: y, //['Residential', 'Non-Residential', 'Utility']
        type: 'pie',
        hoverinfo: 'label+percent',
        textinfo: 'none'
      }];
    var layout = {
      showlegend: showlegend,
      margin: {
        l:0,r:0,b:10,t:10,pad:10
      },
      plot_bgcolor:"#343a40",
      paper_bgcolor: "#343a40",
      height:height,

    };

      return Plotly.newPlot(gd, data, layout, setting);


}
function generate_colors(start,end,step){
  var steps = [
    (end[0]-start[0]) / step ,
    (end[1]-start[1]) / step ,
    (end[2]-start[2]) / step ,
  ];

  var color = [];
  for (var ii =0 ; ii < step  ; ii++ ){
    var _r = Math.floor(start[0] + steps[0] * (ii));
    var _g = Math.floor(start[1] + steps[1] * (ii));
    var _b = Math.floor(start[2] + steps[2] * (ii));
    var _a = 0.8
    var _color = 'rbga('+ _r + ',' + _g + ',' + _b + ',' + _a +')' ;
    color.push(_color);
  }
  return color;

}

function chart_geo(div,width,height,json){
  /*
  div : select  
  */
  if (width > 320){
    width = width
  }
  if (height > 100){
    height = height
  }
    // 23個 縣市 
    /*
    var colors = generate_colors([0,0,0],[10,100,212],json.length);
    console.log(colors);
    */
    var colors = [
      'rgba(240,248,255,0.7)',
      'rgba(250,235,215,0.7)',
      'rgba(0,255,255,0.7)',
      'rgba(127,255,255,0.8)',
      'rgba(245,245,220,0.8)',
      'rgba(255,228,196,0.8)',
      'rgba(255,235,205,0.8)',
      'rgba(0,0,255,0.8)',
      'rgba(138,43,226,0.8)',
      'rgba(165,42,42,0.8)',
      'rgba(222,184,135,0.8)',
      'rgba(95,158,160,0.8)',
      'rgba(127,255,0,0.8)',
      'rgba(210,105,30,0.8)',
      'rgba(255,248,220,0.8)',
      'rgba(220,20,60,0.8)',
      'rgba(0,255,255,0.8)',
      'rgba(0,0,139,0.8)',
      'rgba(184,134,11,0.8)',
      'rgba(169,169,169,0.8)',
      'rgba(0,100,0,0.8)',
      'rgba(189,183,107,0.8)',
      'rgba(139,0,139,0.8)',
      'rgba(85,107,47,0.8)',
      'rgba(255,140,0,0.8)',
    ];
    
    /*
    var layer = json.map(function(x){
      return {
        sourcetype: 'geojson',
        source:x,
        type: 'fill',
        color: 'rgba(127,137,249,0.8)'
      };
    });
    */
    var layer = [];
    for (var a = 0 ; a < json.length; a++) {
      var ly = {
        sourcetype: 'geojson',
        source: json[a],
        type: 'fill',
        color: colors[a]
        };
      layer.push(ly);
    }
    
    var data = [{
        type:'scattermapbox', //scattermapbox
        showlegend:false,
        mode:'markers', // 
        autocolorscale: true,
        marker: {
          size:14,
          colorbar:{
            thickness: 15,
            titleside: 'right',
            outlinecolor: 'rgba(68,68,68,0)',
            ticks: 'outside',
            ticklen: 3,
            shoticksuffix: 'last',
            ticksuffix: '℃',
            dtick: 2
          }
        },
        text:['Taiwan']
      }]
      var layout = {
        autosize: true,
        hovermode:'closest',
        style:'dark',
        mapbox: {
          bearing:0,
          center: {
            lat:23.5,
            lon:121
          },
          pitch:0,
          zoom:6,
          layers: layer
        },
        margin:{
            l:10,r:10,b:10,t:10,pad:20
        },
        height:height,
        width:width-20
      }
      Plotly.setPlotConfig({
        mapboxAccessToken:'pk.eyJ1IjoidHcwMDA4OTkyMyIsImEiOiJjamt1cHgxcXQwM3Q5M3Bta3NqNGswd3IzIn0.HcRKtO-moyhFxQjhHjO9-w'
      })
      return Plotly.plot(div, data, layout,  setting );
}

function draw_plot1(div){

    var xValue = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012];

    var yValue = [16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270, 299, 340, 403, 549, 499];

    var trace1 = {
        x: xValue,
        y: yValue,
        type: 'bar',
        text: yValue,

        hoverinfo: 'none',
        marker: {
            color: 'rgb(158,202,225)',
            opacity: 0.6,
            line: {
            color: 'rbg(8,48,107)',
            width: 1.5
            }
        }
    };

    var data = [trace1];

    var layout = {
        hovermode: false,
        autosize:true,
        xaxis: {
        autorange: true,
        showgrid: false,
        zeroline: false,
        showline: false,
        autotick: true,
        fixedrange : true,
        ticks: '',
        showticklabels: false
      },
      yaxis: {
        autorange: true,

        showgrid: false,
        zeroline: false,
        showline: false,
        autotick: true,
        fixedrange : true,
        ticks: '',
        showticklabels: false
      },
      margin:{
        l:0,r:0,b:10,t:10,pad:10
      },
      plot_bgcolor:"#343a40",
      height:120
    };


    return Plotly.newPlot(div, data, layout, { displayModeBar: false ,scrollZoom: false,editable: false});
}


function draw_hplot(div){


    var trace0 = {
        type: 'bar',
        x: [1, 2, 3, 5.5, 10],
        y: [10, 8, 6, 4, 2],
        width: [0.8, 0.8, 0.8, 0.8, 0.8],
        orientation: 'h'
      }
    var data = [trace0];
    var layout = {
        hovermode: false,
        autosize:true,
        xaxis: {
        autorange: true,
        showgrid: false,
        zeroline: false,
        showline: false,
        autotick: true,
        fixedrange : true,
        ticks: '',
        showticklabels: false
      },
      yaxis: {
        autorange: true,
        showgrid: false,
        zeroline: false,
        showline: false,
        autotick: true,
        fixedrange : true,
        ticks: '',
        showticklabels: false
      },
      margin:{
        l:0,r:0,b:10,t:10,pad:10
      },
      plot_bgcolor:"#343a40",
      height:120
    };


    return Plotly.newPlot(div, data, layout, { displayModeBar: false ,scrollZoom: false,editable: false});
    
    // Function for vertival
    



}