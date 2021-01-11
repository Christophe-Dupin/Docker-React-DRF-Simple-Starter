import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { categories: [] };
  }
  componentDidMount() {
    this.getCategories();
  }
  getCategories() {
    axios
      .get('http://0.0.0.0:8000/api/post/')
      .then(res => {
        this.setState({ categories: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }
  render() {
    return (
      <div>
        {this.state.categories.map(item => (
          <div key={item.id}>
            <h1>{item.body}</h1>
          </div>
        ))}
      </div>
    );
  }
}
export default App;
