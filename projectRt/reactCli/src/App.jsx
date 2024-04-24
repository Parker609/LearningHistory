import React, { Component } from 'react'
import SetState from './components/01SetState'
import LazyLoad from './components/02LazyState'
import Hooks from './components/03Hooks'

export default class App extends Component {
  render() {
    return (
      <div>
        <SetState/>
        <LazyLoad/>
        <Hooks/>
      </div>
    )
  }
}
