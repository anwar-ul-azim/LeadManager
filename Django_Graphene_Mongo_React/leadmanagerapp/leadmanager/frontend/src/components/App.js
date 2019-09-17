import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class App extends Component{
    render(){
        return <h1>basic react app</h1>
    }
}

ReactDOM.render(<App />, document.getElementById('app'));