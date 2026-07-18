"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Loader2, SendHorizontal } from "lucide-react";

type Props = {
  onSend: (message: string) => void;
  loading: boolean;
};

export default function ChatInput({ onSend, loading }: Props) {
  const [question, setQuestion] = useState("");

  function handleSend() {
    if (!question.trim() || loading) return;

    onSend(question);
    setQuestion("");
  }

  return (
    <div className="border-t border-zinc-800 bg-zinc-950 p-4">
      <div className="mx-auto flex max-w-5xl gap-3">
        <Input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              handleSend();
            }
          }}
          placeholder="Ask an NLP question..."
          disabled={loading}
        />

        <Button
          onClick={handleSend}
          disabled={loading}
          className="w-28"
        >
          {loading ? (
            <Loader2 className="h-4 w-4 animate-spin" />
          ) : (
            <>
              <SendHorizontal className="mr-2 h-4 w-4" />
              Send
            </>
          )}
        </Button>
      </div>
    </div>
  );
}