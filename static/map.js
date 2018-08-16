
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
    
   
    return  Plotly.newPlot(gd, data, layout,{ displayModeBar: false ,scrollZoom: false,editable: false});
  

}

function drawCircle(x,y,div){
    var height = 200;
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
      showlegend: false,
      margin: {
        l:0,r:0,b:10,t:10,pad:10
      },
      plot_bgcolor:"#343a40",
      paper_bgcolor: "#343a40",
      height:height
    };

      return Plotly.newPlot(gd, data, layout, { displayModeBar: false ,scrollZoom: false,editable: false});


}
function chart_geo(div){

    var data = [{
        type:'scattermapbox',
        lat:['23 '],
        lon:['121.597366'],
        mode:'markers',
        marker: {
          size:14
        },
        text:['Montreal']
      }]
      
      var layout = {
        autosize: true,
        hovermode:'closest',
        mapbox: {
          bearing:0,
          center: {
            lat:23,
            lon:121.597366
          },
          pitch:0,
          zoom:5
        },

        margin:{
            l:0,r:0,b:10,t:10,pad:10
        },
        height:220,

      }
      Plotly.setPlotConfig({
        mapboxAccessToken:'pk.eyJ1IjoiZXRwaW5hcmQiLCJhIjoiY2luMHIzdHE0MGFxNXVubTRxczZ2YmUxaCJ9.hwWZful0U2CQxit4ItNsiQ'
      })
      return Plotly.plot(div, data, layout, { displayModeBar: false ,scrollZoom: false,editable: false});
      

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