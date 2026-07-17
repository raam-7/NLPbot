import ChatInput from "./ChatInput";
import Message from "./Message";

export default function ChatWindow() {
  return (
    <section className="flex flex-1 flex-col">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-8">
        <div className="mx-auto max-w-4xl space-y-6">
          <Message
            role="assistant"
            content="👋 Hello! I'm your AI NLP Tutor. Ask me anything about Natural Language Processing."
          />
        </div>
      </div>

      {/* Input */}
      <ChatInput />
    </section>
  );
}