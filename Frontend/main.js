const url="http://127.0.0.1:8000/predict"

const msg=document.querySelector('#message')
const button = document.querySelector('.btn-predict')
const box=document.querySelector('.output')
box.classList.remove('.output')
    button.addEventListener("click",async ()=>{
        
        const message_obj={
            message:msg.value
        }
        try{
            let response= await fetch(url, {
                method:"POST",
                headers:{
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(message_obj)
            })
            let result=await response.json()
            if(result.error){
                box.classList.add('.output')
               box.innerText = `Error: ${result.error}`;
            } 
            else{
                box.classList.add('.output')
                box.innerText=`${result.prediction}`
            }
            }
        
        catch (error)
        {
          box.classList.add('.output')
            box.innerText=`${error}`
        }
    })

