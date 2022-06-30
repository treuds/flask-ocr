import React from 'react';
import ThemeProvider from 'react-bootstrap/ThemeProvider';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container'
import { useFileUpload } from 'use-file-upload';

const App = () => {
  const [file, selectFile] = useFileUpload()

  return (
    <ThemeProvider
  breakpoints={['xxxl', 'xxl', 'xl', 'lg', 'md', 'sm', 'xs', 'xxs']}
>
    <Container>
    <Form.Group controlId="formFile" className="mb-3">
    <Form.Label>Default file input example</Form.Label>
    <Form.Control type="file" />
  </Form.Group>
  
     
    <Button
        onClick={() => {
          // Single File Upload accepts only images
          selectFile({ accept: 'image/*' }, ({ source, name, size, file }) => {
            // file - is the raw File Object
            console.log({ source, name, size, file })
            // Todo: Upload to cloud.
          })
        }}
      >
        Click to Upload
      </Button>
      </Container>
    </ThemeProvider>
  )
}

export default App