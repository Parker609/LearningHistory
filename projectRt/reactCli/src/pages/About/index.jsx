import React, { Component } from 'react';
import {Route, Redirect} from 'react-router-dom';
import Idx from '../../components/Idx';
import Msgs from './Msgs';
import News from './News';

export default class About extends Component {
  render() {
    return (
      <div>
        this is About;
        <Idx to="/about/msg">msg</Idx>
        <Idx to="/about/news">msg</Idx>
        <Route path="/about/msg" component={Msgs}></Route>
        <Route path="/about/news" component={News}></Route>
        <Redirect to="/about/news"/>
      </div>
    )
  }
}
