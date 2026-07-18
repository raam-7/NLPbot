"use client";

import { useEffect, useRef } from "react";
import Message from "./Message";
import { ChatMessage } from "@/types/chat";

type Props = {
  messages: ChatMessage[];
};

export default function MessageList({ messages }: Props) {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  return (
    <div className="flex-1 overflow-y-auto">
      <div className="mx-auto max-w-4xl space-y-8 p-8">
        {messages.map((message, index) => (
          <Message
            key={index}
            role={message.role}
            content={message.content}
          />
        ))}

        <div ref={bottomRef} />
      </div>
    </div>
  );
}