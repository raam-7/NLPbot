import { Loader2 } from "lucide-react";

export default function TypingIndicator() {
  return (
    <div className="flex items-center gap-3 px-8 py-4">

      <div className="flex h-10 w-10 items-center justify-center rounded-full bg-zinc-800">
        🤖
      </div>

      <div className="rounded-xl bg-zinc-900 border border-zinc-700 px-4 py-3 flex items-center gap-3">
        <Loader2 className="h-4 w-4 animate-spin" />
        <span className="text-sm text-zinc-400">
          AI is thinking...
        </span>
      </div>

    </div>
  );
}