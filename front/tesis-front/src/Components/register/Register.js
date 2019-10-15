import React from 'react'
import './Register.css'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container'

function Register(){
    return(
        <div>
            <Container>
                <h1 className="global text-center">Register</h1>
                <Form>
                    <Form.Group >
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email"/>
                        <Form.Text classname="text-muted">
                            we'll never share your email with anyone else.
                        </Form.Text>
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Password" />
                    </Form.Group>
                    <Form.Group>
                        <Form.Check type="checkbox" label="Accepts terms of service"/>
                    </Form.Group>
                    <Button variant="primary" type="submit">Register self</Button>
                </Form>
            </Container>
        </div>
    )
}

export default Register 