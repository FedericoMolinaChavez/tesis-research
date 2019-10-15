import React, { Component } from 'react'
import './Login.css'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container'
import {Redirect} from 'react-router-dom'
class Login extends Component{
    constructor(props){
        super(props)
        this.state = {
            red : false 
        }
    }
    render(){
        if(this.state.red === true){
            return(<Redirect to="/Main" />)
        }
        return(
            <div>
                <Container>
                <h1 className="global text-center">login</h1>
                <Form>
                    <Form.Group >
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email"/>
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Password" />
                    </Form.Group>
                    <Button variant="primary" onClick={()=>{ 
                       this.setState({red:true})
                    }}>Log in</Button>
                </Form>
                </Container>
            </div>
        )
    }
    
}

export default Login 