import React, { Fragment } from 'react';
import {Link} from 'react-router-dom';
import './App.css';
import Aside from './components/Layout/Aside';
import Header from './components/Layout/Header'
import { Switch, BrowserRouter as Router, Route } from 'react-router-dom';
import {Layout} from 'antd'
import Login from './pages/Login';
import Register from './pages/Register'

function App() {
  return (
    <Router>
      <Fragment>
        <Switch>
          <Route exact path='/Login' component={Login}/>
          <Route path='/register' component={Register}/>
        </Switch>
      </Fragment>
    </Router>
  );
}

export default App;
