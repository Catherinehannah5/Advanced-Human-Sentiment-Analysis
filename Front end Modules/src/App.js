import ReactDOM from 'react-dom'
import React, { useState } from 'react';
import Button from 'react-bootstrap-button-loader';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'; 
import FusionCharts from "fusioncharts";
import charts from "fusioncharts/fusioncharts.charts";
import ReactFusioncharts from "react-fusioncharts";
import WordCloud from 'react-d3-cloud';
class App extends React.Component {
state = {
    array_keyword_object_with_data: [],
  };
 
  append_keyword = (datareturned) => {
  	this.setState(prevState => ({
    	array_keyword_object_with_data: [...prevState.array_keyword_object_with_data, datareturned],
    }));
  };
  
	render() {
  	return (
      
  <React.Fragment>

    <div id="slide" class="cb-slideshow" >
    <ul class="cb-slideshow" >
    <li>
      <span>1</span>
      {}
    </li>
    <li>      
      <span>2</span>
      {}
      </li>
    <li>      
      <span>3</span>
      {}
      </li>
      <li>      
      <span>4</span>
      {}
      </li>
      <li>      
      <span>5</span>
      {}
      </li>
      <li>      
      <span>6</span>
      {}
      </li>
  </ul>
  </div>

   <div id="root" class="jumbotron text-center">
      <h2><strong>SENTIMENTS AT A GLANCE</strong></h2>
        <p> <i>Welcome to the world of analytics..</i></p>
      <Form onSubmit={this.append_keyword} />  
      <Keyword_list array_keyword_object_with_data={this.state.array_keyword_object_with_data} /> 
  </div>

  

      <span class="glyphicon glyphicon-globe logo"></span>
    <div class="bgsteps">
      {/* <h3 class="text-center"><strong id="stepsfollow">Follow these simple steps:</strong></h3> */}
      <p></p>
      <p></p>
      <p></p>
      <div >
        <div></div>
      <p class="text-left"><img src="1.png" width="100" height="100" class="text-left"/><strong id="step"> Enter Keyword/Topic in search field.</strong></p>
      <p class="text-left"><img src="2.png" width="100" height="100" /><strong id="step"> Visualize what people think about that keyword globally on twitter. </strong></p>
      <p class="text-left"><img src="3.png" width="100" height="100"/><strong id="step"> Explore other features (News, Trending hashtags etc..)</strong></p>

     

 

<div class="text-center">
<img src="Hot_Topic_logo.png" height="50" width="250"></img>
</div>
  {/* <h1 class="text-center">--HOT TOPICS--</h1> */}
  <br></br>
  <div class="row">
<div ></div>
    <div class="col-sm-4" >
      <div id="news01">
      <a href="https://twitter.com/search?q=%23donaldtrump&src=typed_query"><h4 id="colorbt" >DONALD TRUMP</h4></a>
      <div id="opinionp">Positive Opinion: 50% </div>
<div id="opinionn"> Negative Tweets: 50% </div>
<div ><a href="https://www.cnn.com/search?q=donald%20trump&size=10&sort=newest" ><p id="newssize">RELATED NEWS!</p></a></div>
      </div>
    </div>

    <div class="col-sm-4">
    <div id="news01">
      <a href="https://twitter.com/search?q=%23coronavirus&src=typed_query"><h4 id="colorbt">CORONAVIRUS</h4></a>
      <div id="opinionp">Positive Opinion: 50% </div>
<div id="opinionn"> Negative Tweets: 50% </div>
<div ><a href="https://www.cnn.com/search?q=coronavirus&size=10&sort=newest" ><p id="newssize">RELATED NEWS!</p></a></div>

    </div>
</div>
    <div class="col-sm-4">
    <div id="news01">
      <a href="https://twitter.com/search?q=%23climatechange&src=typed_query"><h4 id="colorbt">CLIMATE CHANGE</h4></a>
      <div id="opinionp">Positive Opinion: 50% </div>
<div id="opinionn"> Negative Tweets: 50% </div>
<div ><a href="https://www.cnn.com/search?size=10&q=climate%20change&sort=newest" ><p id="newssize">RELATED NEWS!</p></a></div>

    </div>
</div>
    </div>

    <br></br>

  <div class="row">
    <div class="col-sm-4">
    <div id="news01">
      <a href="https://twitter.com/search?q=%23SocialDistanacing&src=typeahead_click"><h4 id="colorbt">SOCIAL DISTANCING</h4></a>
      <div id="opinionp">Positive Opinion: 50% </div>
<div id="opinionn"> Negative Tweets: 50% </div>
<div ><a href="https://www.cnn.com/search?size=10&q=SOCIAL%20DISTANCING&sort=newest" ><p id="newssize">RELATED NEWS!</p></a></div>


    </div>
</div>
    <div class="col-sm-4">
    <div id="news01">
      <a href="https://twitter.com/search?q=%22247%20canadians%22&src=trend_click"><h4 id="colorbt">247 CANADIANS</h4></a>
      <div id="opinionp">Positive Opinion: 50% </div>
<div id="opinionn"> Negative Tweets: 50% </div>
<div ><a href="https://www.cnn.com/search?size=10&q=CANADIANS&sort=newest" ><p id="newssize">RELATED NEWS!</p></a></div>

    </div>
</div>
    <div class="col-sm-4">
    <div id="news01">
      <a href="https://bing.com/covid"><h4 id="colorbt">COVID-19 TRACKER</h4></a>

      <div id="opinionp">Positive Opinion: 50% </div>
<div id="opinionn"> Negative Tweets: 50% </div>
<div ><a href="https://www.cnn.com/search?size=10&q=COVID-19%20TRACKER&sort=newest" ><p id="newssize">RELATED NEWS!</p></a></div>

</div>
</div>
  </div>
{/* </div> */}

<br></br>
<br></br>
<br></br>
<div class="contact">
<div class="container-fluid bg-grey">
{/* REMOVE ABOVE COMMENT TO MAKE A SOLID BACKGROUND THAT WE HAVE DONE EARLIER */}

  <h1 class="text-center" id="inner2"><strong>CONTACT US</strong></h1>
  <div class="row">
    <div class="col-sm-5" >
      <p id="inner2">Contact us for adding new functionality or any other issues you are facing while doing the analysis.</p>
      <p id="inner2"> <span class="glyphicon glyphicon-map-marker"></span> Waterloo, ON</p>
      <p id="inner2"><span class="glyphicon glyphicon-phone"></span> +1 222332433434</p>
      <p id="inner2"><span class="glyphicon glyphicon-envelope"></span> info@humansentiment.com</p>
    </div>
    <div class="col-sm-7">
      <div class="row">
        <div class="col-sm-6 form-group">
          <input class="form-control" id="name" name="name" placeholder="Name" type="text" required></input>
        </div>
        <div class="col-sm-6 form-group">
          <input class="form-control" id="email" name="email" placeholder="Email" type="email" required></input>
        </div>
      </div>
      <textarea class="form-control" id="comments" name="comments" placeholder="Comment" rows="5"></textarea><br></br>
      <div class="row">
        <div class="col-sm-12 form-group">
          <button class="btn btn-danger" type="submit" >Send</button>
          
        </div>
      </div>
    </div>
  </div>
</div>
</div>

<footer id="footer" >

    <p  id="inner1" class="news1"><p id="inner1">Disclaimer</p><p id="inner1">If you require any more information or have any questions about our site's disclaimer, please feel free to contact us by email at info@humansentiment.com. 
    All the information on this website - Humansentiment.com - is published in good faith and for general information purpose only. Human Sentiment does not make any warranties about the completeness, 
    reliability and accuracy of this information. Any action you take upon the information you find on this website (Human Sentiment), is strictly at your own risk. Human Sentiment will not be liable for any losses and/or damages 
    in connection with the use of our website. Our Disclaimer was generated with the help of the Disclaimer Generator. From our website, you can visit other websites by following hyperlinks to such external sites. While we strive to 
    provide only quality links to useful and ethical websites, we have no control over the content and nature of these sites.
    </p>
</p>
</footer>
{/* </div> */}

</React.Fragment>
    );
  }	
}

class Company extends React.Component {
	render() {
    const p = this.props;
    
    charts(FusionCharts);
    const dataSource = {
      chart: {
        caption: "TWEETS SENTIMENT",
        subcaption: "Percentage of Highly Positive, Highly Negative, Neutral, Positive and Negative tweets",
        showvalues: "1",
        showpercentintooltip: "0",
        numbersuffix: "%",
        enablemultislicing: "1",
        theme: "fusion"
      },
      data: [
        {
          label: "Highly Negative Tweets",
          value: p.Pie_Chart.Highly_NT_df
        },
        {
          label: "Highly Positive Tweets",
          value: p.Pie_Chart.Highly_PT_df
        },
        {
          label: "Neutral Tweets",
          value: p.Pie_Chart.Neut_df
        },
        {
          label: "Slightly Negative Tweets",
          value: p.Pie_Chart.Slightly_NT_df
        },
        {
          label: "Slightly Positive Tweets",
          value: p.Pie_Chart.Slightly_PT_df
        }
      ]
    };


    const data = [

      {
        text: p.Word_Cloud[0],
        value: 64,
      },
      {
        text: p.Word_Cloud[1],
        value: 11,
      },
      {
        text: p.Word_Cloud[2],
        value: 64,
      },
      {
        text: p.Word_Cloud[3],
        value: 11,
      },
      {
        text: p.Word_Cloud[4],
        value: 64,
      },
      {
        text: p.Word_Cloud[5],
        value: 11,
      },
      {
        text: p.Word_Cloud[6],
        value: 64,
      },
      {
        text: p.Word_Cloud[7],
        value: 11,
      },
      {
        text: p.Word_Cloud[8],
        value: 64,
      },
      {
        text: p.Word_Cloud[9],
        value: 11,
      },
      {
        text: p.Word_Cloud[10],
        value: 64,
      },
      {
        text: p.Word_Cloud[11],
        value: 11,
      },
      {
        text: p.Word_Cloud[12],
        value: 64,
      },
      {
        text: p.Word_Cloud[13],
        value: 11,
      },
      {
        text: p.Word_Cloud[14],
        value: 64,
      },
      {
        text: p.Word_Cloud[15],
        value: 11,
      },
      {
        text: p.Word_Cloud[16],
        value: 64,
      },
      {
        text: p.Word_Cloud[17],
        value: 11,
      },
      {
        text: p.Word_Cloud[18],
        value: 64,
      },
      {
        text: p.Word_Cloud[19],
        value: 11,
      },
      {
        text: p.Word_Cloud[20],
        value: 64,
      },
      {
        text: p.Word_Cloud[21],
        value: 11,
      },

      
      {
        text: p.Word_Cloud[22],
        value: 64,
      },
      {
        text: p.Word_Cloud[23],
        value: 11,
      },
      {
        text: p.Word_Cloud[24],
        value: 64,
      },
      {
        text: p.Word_Cloud[25],
        value: 11,
      },
      {
        text: p.Word_Cloud[26],
        value: 64,
      },
      {
        text: p.Word_Cloud[27],
        value: 11,
      },
      {
        text: p.Word_Cloud[28],
        value: 64,
      },
      {
        text: p.Word_Cloud[29],
        value: 11,
      },
      {
        text: p.Word_Cloud[30],
        value: 64,
      },
      {
        text: p.Word_Cloud[31],
        value: 11,
      },
      {
        text: p.Word_Cloud[32],
        value: 64,
      },
      {
        text: p.Word_Cloud[33],
        value: 11,
      },
      {
        text: p.Word_Cloud[34],
        value: 64,
      },
      {
        text: p.Word_Cloud[35],
        value: 11,
      },
      {
        text: p.Word_Cloud[36],
        value: 64,
      },
      {
        text: p.Word_Cloud[37],
        value: 11,
      },
      {
        text: p.Word_Cloud[38],
        value: 64,
      },
      {
        text: p.Word_Cloud[39],
        value: 11,
      },
      {
        text: p.Word_Cloud[40],
        value: 64,
      },
      {
        text: p.Word_Cloud[41],
        value: 11,
      },
      {
        text: p.Word_Cloud[42],
        value: 64,
      },
      {
        text: p.Word_Cloud[43],
        value: 11,
      },
      {
        text: p.Word_Cloud[44],
        value: 11,
      },
      {
        text: p.Word_Cloud[45],
        value: 64,
      },
      {
        text: p.Word_Cloud[46],
        value: 11,
      },
      {
        text: p.Word_Cloud[47],
        value: 64,
      },
      {
        text: p.Word_Cloud[48],
        value: 11,
      },
      {
        text: p.Word_Cloud[49],
        value: 64,
      },
      {
        text: p.Word_Cloud[50],
        value: 11,
      },
      {
        text: p.Word_Cloud[51],
        value: 64,
      },
      {
        text: p.Word_Cloud[52],
        value: 11,
      },
      {
        text: p.Word_Cloud[53],
        value: 11,
      },
      {
        text: p.Word_Cloud[54],
        value: 64,
      },
      {
        text: p.Word_Cloud[55],
        value: 11,
      },
      {
        text: p.Word_Cloud[56],
        value: 64,
      },
      {
        text: p.Word_Cloud[57],
        value: 11,
      },
      {
        text: p.Word_Cloud[58],
        value: 64,
      },
      {
        text: p.Word_Cloud[59],
        value: 11,
      },    
    ];
    
    
    
    const fontSizeMapper = word => Math.log2(word.value) * 6;
    const rotate = word => word.value % 100 ;
return(
 <div >
  
    {/* fusion chart  */}
    <br></br>
    <br></br>
    <ReactFusioncharts
        type="pie3d"
        width="80%"
        height="10%"
        dataFormat="JSON"
        dataSource={dataSource}
      />
      <br></br>
      <br></br>
      <br></br>
      <div class="wordc"> 
      <h1>WORD CLOUD</h1>
      
      </div> 
      <div class="word1">
      <WordCloud
    data={data}
    fontSizeMapper={fontSizeMapper}
    rotate={rotate}
  />
  </div>
  <div >
  <div class="container-fluid bg-secondary">

<span class="glyphicon glyphicon-globe logo"></span>
{/* <div class="container-fluid bg-secondary"> */}
<h3><strong>-- TRENDING NEWS--</strong></h3>
<div class="news1">

      <div class="newsall"><ul>{p.News[0]}</ul></div>
      </div>
      <div class="news1">

      <div class="newsall"><ul>{p.News[1]}</ul></div>
      </div>

      <div class="news1">
      <div class="newsall"><ul>{p.News[2]}</ul></div>
      </div>

      <div class="news1">
      <div class="newsall"><ul>{p.News[3]}</ul></div>
      </div>

      <div class="news1">
      <div class="newsall"><ul>{p.News[4]}</ul></div>
      </div>

      <div class="news1">
      <div class="newsall"><ul>{p.News[5]}</ul></div>
      </div>

      <div class="news1">

      <div class="newsall"><ul>{p.News[6]}</ul></div>
      </div>

      <div class="news1">

      <div class="newsall"><ul>{p.News[7]}</ul></div>
      </div>

      <div class="news1">

      <div class="newsall"><ul>{p.News[8]}</ul></div>
      </div>

      <div class="news1">

      <div class="newsall"><ul>{p.News[9]}</ul></div>
      </div>

      <div class="news1">

      <div class="newsall"><ul>{p.News[10]}</ul></div>
      </div>

      <div class="news1">

      <div class="newsall"><ul>{p.News[11]}</ul></div>
      </div>

      <div class="news1">

      <div class="newsall"><ul>{p.News[12]}</ul></div>
      </div>

      <div class="news1">

      <div class="newsall"><ul>{p.News[13]}</ul></div>
      </div>

      <div class="news1">

      <div class="newsall"><ul>{p.News[14]}</ul></div>
      </div>

            <div class="news1">

      <div class="newsall"><ul>{p.News[15]}</ul></div>



  </div>
</div>
      </div>
  <div className='app-inner'>
      
        <div className="datareturned">
         
          <div></div>
        </div>
    	</div>
      </div>
    );
  }
}


class Keyword_list extends React.Component {
  render() {
    // const p = t/his.state.resp1;
    const p = this.props;
      return (
          <div className="companylist">
            
          <span className="companylisttext"></span>
          {p.array_keyword_object_with_data.map(datareturned => <Company key={datareturned.id} {...datareturned}/>)}
          </div>
      );
  }
}


class Form extends React.Component {
  state = { user_keyword: ''};  //1


  handleSubmit = async (event) => {    //2  using hooks . it becomes simpler  ASYNCHRONOUS F UNCTION https://medium.com/@ian.mundy/async-event-handlers-in-react-a1590ed24399
    event.preventDefault();
    console.log(this.user_keyword)
    const resp = await axios.get(`http://localhost:5000/word?place=${this.state.user_keyword}`, {headers:{'Access-Control-Allow-Origin':'*'}});
    this.props.onSubmit(resp.data);  
    console.log(this.props.p)
    // this.setState({resp1:resp})                                                                                   //take data from the api and pass it to onsubmit  
    this.setState({ user_keyword: '' });
  };
 	render() {
  	return (
//2
    	<form onSubmit={this.handleSubmit}  >

      <div class="input-group">
      <span className="formtext"></span>
    	  <input 
          type="text" 
          value={this.state.user_keyword}    //1
          onChange={event => this.setState({ user_keyword: event.target.value })}   //1
          //<input value={this.state.value} onChange={this.handleChange} />
          placeholder="Enter keywords.." 
          class="form-control"
          size="50"
          required 
        />

        <button type="submit" class="btn btn-danger" >DO Analysis!!</button>
      </div>
    	</form>
    );
  }
}
export default App;








