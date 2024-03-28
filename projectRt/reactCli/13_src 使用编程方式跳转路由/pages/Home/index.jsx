import React, { Component } from 'react'

export default class index extends Component {
  render() {
    console.log(this.props.location.state)
    return (
      <div>
        this is Home
      </div>
    )
  }
}
