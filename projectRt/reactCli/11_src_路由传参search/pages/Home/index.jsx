import React, { Component } from 'react'

export default class index extends Component {
  render() {
    // search参数在location的search中；由用户解开；
    console.log(this.props.location.search)
    return (
      <div>
        this is Home
      </div>
    )
  }
}
