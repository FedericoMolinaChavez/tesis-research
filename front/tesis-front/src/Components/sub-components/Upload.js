import React, { Component } from "react";
import Dropzone from "./Dropzone";
import "./Upload.css";
import Progress from './Progress';
import Button from 'react-bootstrap/Button'
class Upload extends Component {
  
  stringLenguage = []

  constructor(props) {
    super(props);
    this.state = {
      files: [],
      uploading: false,
      uploadProgress: {},
      successfullUploaded: false,
      isPhoto: false,
      premium: false,
      tipoDeConsulta: '',
      clasificacion: '',
      lenguage: 'en' 
    };

    this.onFilesAdded = this.onFilesAdded.bind(this);
    this.uploadFiles = this.uploadFiles.bind(this);
    this.sendRequest = this.sendRequest.bind(this);
    this.renderActions = this.renderActions.bind(this);
    this.uploadImages = this.uploadImages.bind(this);
  }

  onFilesAdded(files) {
    this.setState(prevState => ({
      files: prevState.files.concat(files)
    }));
  }
  async uploadImages() {
    await this.setState({isPhoto : true})
    this.setState({ uploadProgress: {}, uploading: true });
    let promises = [];
    await this.state.files.forEach(file => {
      promises.push(this.mixAll2(file));
    });
    try {
      await this.sendToServer(promises)
      await this.setState({ successfullUploaded: true, uploading: false });
    } catch (e) {
      // Not Production ready! Do some error handling here instead...
      await this.setState({ successfullUploaded: true, uploading: false });
    }
    //////////console.log('aquí')
    fetch('http://localhost:8080/multipartpdf',{
      method: 'GET',
      headers: {Accept : 'application/x-www-form-urlencoded'},
    }).then(res => {return res.blob()})
    .then(async res => { 
      const file = new Blob(
       [res]
      )
      //////////console.log(file)
      this.setState({isPhoto : false})
      const filename = "pdfgenerated.pdf"
      promises = []
      await promises.push(this.mixall3(file,filename))
      try {
        await this.sendToServer(promises)
      }
      catch (e){
        ////////console.log(e)
      }

    //////////console.log(pdf)

    this.setState({isPhoto : false})
    
    }) 
  }
    
  

  async uploadFiles() {
    this.setState({ uploadProgress: {}, uploading: true });
    const promises = [];
    this.state.files.forEach(file => {
      promises.push(this.mixAll(file));
    });
    try {
      this.sendToServer(promises)
      this.setState({ successfullUploaded: true, uploading: false });
    } catch (e) {
      // Not Production ready! Do some error handling here instead...
      this.setState({ successfullUploaded: true, uploading: false });
    }
  }

  mixAll = (file) => {
    let divide = file.name.split('.')
    const formData = new FormData();
      formData.append("date",this.props.date)
      formData.append("cr", file, divide[0]+'-' + this.props.userName+'-'+this.state.tipoDeConsulta+'-'+this.state.clasificacion+'-'+this.props.esp+'-'+this.props.date+'-' +this.props.current +'.'+ divide[1]);
      formData.append("nombreArchivo", divide[0]+'-' + this.props.userName+'-'+this.state.tipoDeConsulta+'-'+this.state.clasificacion+'-'+this.props.esp+'-'+this.props.date+'-' +this.props.current +'.'+ divide[1])
      formData.append('UserToken',this.props.current)
      return(formData)
  }

  mixAll2 = (file) => {
    let divide = file.name.split('.')
    const formData = new FormData();
      formData.append("date",this.props.date)
      formData.append("cr", file, divide[0]+'-' + this.props.userName+'-'+this.state.tipoDeConsulta+'-'+this.state.clasificacion+'-'+this.props.esp+'-'+this.props.date+'-' +this.props.current +'.'+ divide[1]);
      formData.append("nombreArchivo", divide[0]+'-' + this.props.userName+'-'+this.state.tipoDeConsulta+'-'+this.state.clasificacion+'-'+this.props.esp+'-'+this.props.date+'-' +this.props.current +'.'+ divide[1])
      formData.append('UserToken',this.props.current)
      return(formData)
  }

  mixall3 = (file,filename) => {
    let divide = filename.split('.')
    const formData = new FormData()
    formData.append("date", this.props.date)
    formData.append("cr", file, divide[0]+'-' + this.props.userName+'-'+this.state.tipoDeConsulta+'-'+this.state.clasificacion+'-'+this.props.esp+'-'+this.props.date+'-' +this.props.current +'.'+ divide[1]);
    formData.append("nombreArchivo", divide[0]+'-' + this.props.userName+'-'+this.state.tipoDeConsulta+'-'+this.state.clasificacion+'-'+this.props.esp+'-'+this.props.date+'-' +this.props.current +'.'+ divide[1])
    formData.append('UserToken',this.props.current)
    return(formData)
  }

  sendToServer(promises){
    
    promises.forEach(async file => {
      ////////console.log("si entra")
      if(this.state.isPhoto === false){
        await this.sendIndividualFile(file)
      }
      else{
        await this.sendIndividualPhoto(file)
      }
      
    })
  }



  sendIndividualFile(file){
    fetch('https://login.keepsafeco.org/route',{
      method: 'POST',
      body: file
    })
  }
  sendIndividualPhoto(file){
    fetch('http://localhost:8080/multipartpdf',
    {method: 'POST',
    body: file}).then(async res => await console.log(res) )
  }

  testConnection(){
    fetch('https://login.keepsafeco.org/route',{
      method: 'GET',
      headers: {
        Accept: '*/*'
      }
    }).then(res => {
      ////////console.log(res)
    })
  }
  sendRequest(file) {
    return new Promise((resolve, reject) => {
      const req = new XMLHttpRequest();

      req.upload.addEventListener("progress", event => {
        if (event.lengthComputable) {
          const copy = { ...this.state.uploadProgress };
          copy[file.name] = {
            state: "pending",
            percentage: (event.loaded / event.total) * 100
          };
          this.setState({ uploadProgress: copy });
        }
      });

      req.upload.addEventListener("load", event => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "done", percentage: 100 };
        this.setState({ uploadProgress: copy });
        resolve(req.response);
      });

      req.upload.addEventListener("error", event => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "error", percentage: 0 };
        this.setState({ uploadProgress: copy });
        reject(req.response);
      });

      const formData = new FormData();
      formData.append("cr", file);
      formData.append("nombreArchivo", file.name+this.props.permits[0].token)

      req.open("POST", "https://login.keepsafeco.org/route");
      req.send(formData);
    });
  }

  renderProgress(file) {
    const uploadProgress = this.state.uploadProgress[file.name];
    if (this.state.uploading || this.state.successfullUploaded) {
      return (
        <div className="ProgressWrapper">
          <Progress progress={uploadProgress ? uploadProgress.percentage : 0} />
          <img
            className="CheckIcon"
            alt="done"
            src="baseline-check_circle_outline-24px.svg"
            style={{
              opacity:
                uploadProgress && uploadProgress.state === "done" ? 0.5 : 0
            }}
          />
        </div>
      );
    }
  }

  renderActions() {
    if (this.state.successfullUploaded) {
      return (
        <div className="buttonContainer">
          <button className="button3" onClick={() => this.setState({ files: [], successfullUploaded: false }) }>{this.stringLenguage[34]}</button>
        </div>
      );
    } else {
      if (!this.props.DoctorPremium) {
        return (
          <div className="buttonContainer">
            <button className="button1" disabled={this.state.files.length < 0 || this.state.uploading} onClick={this.uploadFiles}>{this.stringLenguage[24]}</button>
            <button className="button2NoPremium">{this.stringLenguage[28]}</button>
            <button className="button2NoPremium">{this.stringLenguage[29]}</button>
          </div>
        );
      }else{
        return (
          <div className="buttonContainer">
            <button className="button1" disabled={this.state.files.length < 0 || this.state.uploading} onClick={this.uploadFiles}>{this.stringLenguage[24]}</button>
            <button className="button1" onClick = {this.uploadImages}>{this.stringLenguage[28]}</button>
            <button className="button1" onClick = {this.uploadFiles}>{this.stringLenguage[29]}</button>
          </div>
        );
      }
    }
  }

  render() {

    

    return (
      <div className="Upload">

        <div className="Content">
          <div className="UploadFiles">
            <Dropzone onFilesAdded={this.onFilesAdded} disabled={this.state.uploading || this.state.successfullUploaded} />
          </div>
          <div className="Files">
            {this.state.files.map(file => {
              return (
                <div key={file.name} className="Row">
                  <span className="Filename">{file.name}</span>
                  {this.renderProgress(file)}
                </div>
              );
            })}
          </div>
        </div>
        <p className="global">Drag the file for upload</p>
                    <Button className="global">Upload</Button>
      </div>
    );
  }
}


export default Upload;