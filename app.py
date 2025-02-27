"""
[보고서 기반 AI 의료 상담 시스템 데모]
"""

import gradio as gr
from openai import OpenAI

############################
# 1. OpenAI 클라이언트 설정
############################

client = OpenAI(api_key="")  # 실제 API 키 입력
MODEL_NAME = "gpt-4o"  

############################
# 2. 시스템 메시지(프롬프트) 정의
############################

system_prompt = {
    "role": "system",
    "content": (
        "당신은 의료 상담 보조 시스템입니다. "
        "사용자가 증상을 설명하면, 가능한 질병 가설과 약물 정보를 제공할 수 있습니다. "
        "단, 당신은 실제 의사가 아니므로 모든 답변 뒤에는 전문의와 상의하라는 권고를 해야 합니다. "
        "또한, 잘못된 정보로 인해 발생할 수 있는 문제에 대해 책임지지 않는다는 점을 밝히세요. "
        "진단을 시도할 때는 안전과 정확성을 위해 추가 질문을 하거나, 부족한 정보가 있으면 명확히 지적해주세요. "
        "결정적 증거가 없는 경우, '가능성' 기반으로만 제시하시고, 구체적 처방보다는 OTC(일반 의약품) 수준에서 권장하세요. "
        "기밀 유지와 윤리 가이드라인을 준수하세요."
    )
}

############################
# 3. 대화 이력 초기화
############################

def init_conversation():
    """
    대화 초기: system 메시지를 포함한 리스트를 반환
    """
    return [system_prompt]

############################
# 4. GPT-4o와의 대화 함수
############################

def chat_with_ai(user_input, conversation_history):
    """
    사용자 입력과 기존 대화 기록을 받아, GPT에 질의 후 응답.
    Multi-turn 대화를 위해 conversation_history를 갱신 후 반환.
    """

    # 사용자 메시지 추가
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # GPT API 호출
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=conversation_history
    )

    # GPT 응답 추출
    assistant_message = response.choices[0].message.content

    # 대화 이력에 AI 답변 추가
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    # 갱신된 대화 이력, AI 응답 반환
    return conversation_history, assistant_message

############################
# 5. Gradio UI 설계
############################

def user_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## 의료 진단 AI 시스템 (데모)")

        # (1) 대화 이력을 State로 관리
        conversation_state = gr.State(init_conversation())

        # (2) 채팅 출력 영역 - type="messages" 적용
        chat_display = gr.Chatbot(
            label="의료 상담 봇",
            height=400,
            type="messages"
        )

        # (3) 사용자 입력 + 전송 버튼
        user_input = gr.Textbox(
            lines=2,
            placeholder="증상을 입력해주세요 (예: 머리가 아프고 열이 납니다)",
            label="사용자 입력"
        )
        submit_btn = gr.Button("전송")

        # (4) 응답 처리 함수
        def respond(user_text, conv_hist):
            updated_history, _ = chat_with_ai(user_text, conv_hist)

            messages_for_display = []
            for msg in updated_history:
                # system 메시지는 실제 채팅창에 표시하지 않음
                if msg["role"] == "system":
                    continue
                # user/assistant 메시지는 그대로 표시
                messages_for_display.append({
                    "role": msg["role"],       
                    "content": msg["content"]  # 실제 내용
                })

            # Gradio의 Chatbot outputs
            return updated_history, messages_for_display

        # (5) 전송 버튼 / Enter 이벤트
        submit_btn.click(
            fn=respond,
            inputs=[user_input, conversation_state],
            outputs=[conversation_state, chat_display]
        )
        user_input.submit(
            fn=respond,
            inputs=[user_input, conversation_state],
            outputs=[conversation_state, chat_display]
        )

        # (6) 하단 면책조항
        gr.Markdown("""
        ---
        **주의/면책 조항**  
        본 시스템은 실제 의료 진단이나 처방을 대체할 수 없습니다.  
        증상이 심각하거나 불확실하다면 반드시 전문가와 상담하세요.  
        """)

    return demo

############################
# 6. main 함수
############################

def main():
    demo = user_interface()
    demo.launch(server_name="127.0.0.1", server_port=7860)

if __name__ == "__main__":
    main()
