import { CSRF_TOKEN } from "./csrf_token.js"

function handleResponse(response) {
  if (response.status === 204) {
    throw new Error("No data")
  } else if (response.status === 404) {
    throw new Error("Wrong URL")
  } else if (response.status === 400) {
    throw new Error("Restaurant allready added!")    
  } else {
    return response.json();    
  }
}


function apiService(endpoint, method, data) {
  const config = {
    method: method || "GET",    
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      'content-type': 'application/json',      
      'X-CSRFTOKEN': CSRF_TOKEN,      
    },
  }
  return fetch(endpoint, config)
          .then(handleResponse)
          .catch(error => console.log(error))
}

export { apiService };