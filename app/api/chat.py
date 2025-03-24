from fastapi import APIRouter, Depends, HTTPException
from app.models.chat import ChatRequest, ChatResponse
from app.services.deepseek import DeepseekService

router = APIRouter()
deepseek_service = DeepseekService()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Process a chat request and return a response from the AI model in Bengali with an angry tone.
    """
    try:
        # Add system message to make responses Bengali and angry
        bengali_angry_instruction = {"role": "system", "content": "You are an assistant who always responds in Bengali language with an angry and frustrated tone. Your answers should express annoyance while still providing helpful information. Use Bengali script only."}
        
        # Insert the instruction at the beginning of messages if it's not already there
        messages = request.messages.copy()
        if not messages or messages[0].role != "system":
            messages.insert(0, bengali_angry_instruction)
        
        result = await deepseek_service.generate_response(
            messages=messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )
        
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
            
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))