import React, { useState } from 'react';
import { createUseStyles } from 'react-jss';
import BasicInput from './BasicInput';
import messageDetails from '../messageDetails.json';
import {addMessageToQueue} from '../modules/queueManagement'

const useStyles = createUseStyles({
  message: {
    display: 'flex',
    flexDirection: 'column',
    margin: '10px'
  },
  button: {
    textAlign: 'center',
    margin: '10px',
  }
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
    addMessageToQueue(jsonMessage)
  };

  return <>
    <form onSubmit={handleSubmit}>
      <div className={css.message}>
        {
          Object.keys(message).map((obj, index) => (
            <BasicInput name={obj} value={obj.value} onChange={handleInputChange} key={index}></BasicInput>
          ))
        }
      </div>
      <button type="submit" className='css.button'>Send</button>
    </form>
  </>;
};

export default Form;
