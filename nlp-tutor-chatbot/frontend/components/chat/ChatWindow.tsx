"use client";

import ChatInput from "./ChatInput";
import MessageList from "./MessageList";
import WelcomeScreen from "./WelcomeScreen";
import TypingIndicator from "./TypingIndicator";

import { useChat } from "@/hooks/useChat";

export default function ChatWindow() {
  const { messages, loading, send } = useChat();

  return (
    <section className="flex flex-1 flex-col bg-zinc-950">
      {messages.length === 0 ? (
        <WelcomeScreen />
      ) : (
        <>
          <MessageList messages={messages} />
          {loading && <TypingIndicator />}
        </>
      )}

      <ChatInput
        onSend={send}
        loading={loading}
      />
    </section>
  );
}