import ReactDOM from 'react-dom'
import React, { useState } from 'react';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'; // version boot react problem
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

    <div id="root" class="jumbotron text-center">
      <h1>We do sentiment Analysis</h1>
        <p> Twitter, Facebook..</p>
      <Form onSubmit={this.append_keyword} />  
      <Keyword_list array_keyword_object_with_data={this.state.array_keyword_object_with_data} /> 
    </div>
    {/* <div id="second" class="container-fluid">
      <h2>About Company</h2>
      <h4>Hello boi</h4>
      <p> hello boi2 </p>
      <button class="btn btn-default btn-lg">Get in Touch</button>
      </div> */}
{/* 
      <div id="third" class="container-fluid bg-grey">
          <h2>Data analysis </h2>
          <h4><strong>MISSION:</strong> provide better insights on public opiniopn..</h4>
          <p><strong>VISION:</strong> Become a data management center</p>
      </div> */}
    </React.Fragment>
    );
  }	
}
class Company extends React.Component {
	render() {
  	const p = this.props;
  	return (
    	<div className="company">
        <span className="companytext">&#x3C;Company /&#x3E;</span>
    	  <img src={p.avatar_url} />
        <div className="datareturned">
          <div>Name: {p.name}</div>
          <div>Email: {p.email}</div>
          <div>Bio: {p.bio}</div>
          <div>Repos: {p.public_repos}</div>
        </div>
    	</div>
    );
  }
}
class Keyword_list extends React.Component {
  render() {
    const p = this.props;
      return (
          <div className="companylist">
            
          <span className="companylisttext">&#x3C;Keyword /&#x3E;</span>
          {p.array_keyword_object_with_data.map(datareturned => <Company key={datareturned.id} {...datareturned}/>)}
          </div>
      );
  }
}

class Form extends React.Component {
  state = { user_keyword: '' };  //1


  handleSubmit = async (event) => {    //2  using hooks . it becomes simpler  ASYNCHRONOUS F UNCTION https://medium.com/@ian.mundy/async-event-handlers-in-react-a1590ed24399
    event.preventDefault();
    const resp = await axios.get(`https://api.github.com/users/${this.state.user_keyword}`);
    this.props.onSubmit(resp.data);                                                                                     //take data from the api and pass it to onsubmit  
    this.setState({ user_keyword: '' });
  };
 	render() {
  	return (
//2
    	<form onSubmit={this.handleSubmit}>    
      <div class="input-group">
      <span className="formtext">&#x3C;Form /&#x3E;</span>
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
        <button type="button" class="btn btn-danger">DO Analysis!!</button>
      </div>
    	</form>
    );
  }
}



export default App;
