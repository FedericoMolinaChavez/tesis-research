import React from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Login from './Components/Login/Login'
import Register from './Components/register/Register'
import Main from './Components/Main/Main'
function App() {
  return (
   
      <Router> 
          <div>
          <ul>
          <li>
            <Link to="/">Login</Link>
          </li>
          <li>
            <Link to="/home">Register</Link>
          </li>
        </ul>
          <Switch>
          <Route path exact = "/" component={Login}/>
          <Route path = "/home" component={() => <Register/>}/>
          <Route path= "/main" component={Main}/>
          </Switch>
          </div>
      </Router>
   
  );
}

export default App;
