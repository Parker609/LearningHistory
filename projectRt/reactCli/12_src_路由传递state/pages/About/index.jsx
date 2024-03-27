import React, { Component } from 'react';

export default class About extends Component {
  render() {
    // 通过state传递进来的；
    console.log(this.props.location.state)
    return (
      <div>
        this is About;
      </div>
    )
  }
}
