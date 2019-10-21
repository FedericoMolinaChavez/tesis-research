import React,{Component} from 'react'
import Jumbotron from 'react-bootstrap/Jumbotron'
import Button from 'react-bootstrap/Button'
import Container from 'react-bootstrap/Container'
import Upload from '../sub-components/Upload'
import Form from 'react-bootstrap/Form'
import './Main.css'
class Main extends Component{
    constructor(props){
        super(props)
        this.state = {
            fileName : ''
        }
    }
    processFile = () => {
        fetch('http://localhost:8000/upload',{
            method : 'POST',
            credentials: 'same-origin',
            headers: {'Content-Type': 'application/json', 'Access-Control-Expose-Headers': 'X-Custom-Header'},
            body : JSON.stringify({
              fileName : this.state.fileName,
            })
          })
    .then(ans => ans.json())
    .then(ans => {
        console.log(ans)
    })
        }
    render(){
        return(
            <div>
                <Container type="text">
                    <div className="centered">
                        <h1 className="global text-center">Automatic clivage site predictor</h1>
                    </div>                
                    <Jumbotron>
                        <h2 className="global text-center">Uploading files</h2>
                        <Upload />
                    </Jumbotron>
                </Container>
                <Container>
                    <h2 className="global text-center">Predict</h2>
                    <p className="global">For making a prediction insert the name of the file in the form</p>
                    <Form>
                        <Form.Group>
                            <Form.Label className="global">Name of file</Form.Label>
                            <Form.Control type="text" className="global" placeholder="Enter file name" onChange={(val) => {console.log(this.setState({fileName : val.target.value}))}}/>
                        </Form.Group>
                        <div className="centering">
                            <Button className="global" onClick={()=>{this.processFile()}}>Process</Button>
                        </div>
                    </Form>
                </Container>
            </div>
        )
    }
}

export default Main