import React, { useState } from 'react';
import { createUseStyles } from 'react-jss';
import messageDetails from '../messageDetails.json';
import { sendToRabbit } from '../modules/sendToRabbit';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { grey } from '@mui/material/colors';
import { Button,TextField } from '@mui/material';
import logo from '../images/logo.png';

const useStyles = createUseStyles({
  title:{
    fontSize: '35px',
    marginBottom: '20px'
  },
  message: {
    display: 'flex',
    flexDirection: 'column',
    marginBottom: '30px',
    height:'400px',
    justifyContent: 'space-between',
    width:'50%'
  },
  wrap_form:{
    height: '99vh'
  },
  form:{
    width:'500px',
    backgroundColor: '#8080803b',
    padding: '30px 50px ',
    boxShadow: 'inset 0 -3em 3em rgb(125 141 125 / 30%), 0 0 0 2px white, 0.3em 0.3em 1em rgb(104 102 102 / 60%)'
  },
  flex_item:{
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    flexDirection: 'column',
  },
  logo:{
    position: 'absolute',
    width: '200px'
  }
});

const theme = createTheme({
  palette: {
    primary: grey
  },
});


const Form = () => {
  const css = useStyles();
  const [message, setMessage] = useState(messageDetails.messageDetails);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setMessage({ ...message, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const jsonMessage = JSON.stringify(message);
    sendToRabbit(jsonMessage);
  };

  return <>
    <div><img src={logo} className={css.logo}/></div>
    <div className={[css.wrap_form, css.flex_item].join(' ')}>
      <form onSubmit={handleSubmit} className={[css.form, css.flex_item].join(' ')}>
        <div className={css.title}>
          GPKG-pipeline
        </div>
        <div className={css.message}>
          {
            Object.keys(message).map((obj, index) => (
              <TextField name={obj} value={obj.value} label={obj} onChange={handleInputChange} key={index} margin="dense" required variant="standard"></TextField>
            ))
          }
        </div>
        <div>
          <ThemeProvider theme={theme}>
            <Button variant="contained" type="submit" color="primary" style={{height: '40px', width : '150px'}}>Send</Button>
          </ThemeProvider>
        </div>
      </form>
    </div>
  </>;
};

export default Form;
