import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";

export default function Sidebar() {
  return (
    <aside className="w-72 border-r border-zinc-800 bg-zinc-900 flex flex-col">

      <div className="p-5">

        <h1 className="text-2xl font-bold">
          🧠 NLP Tutor
        </h1>

        <Button className="mt-6 w-full">
          + New Chat
        </Button>

      </div>

      <Separator />

      <div className="flex-1 overflow-y-auto p-4">

        <p className="mb-3 text-xs uppercase text-zinc-500">
          Today
        </p>

        <button className="mb-2 w-full rounded-lg p-3 text-left hover:bg-zinc-800">
          What is Tokenization?
        </button>

        <button className="mb-2 w-full rounded-lg p-3 text-left hover:bg-zinc-800">
          Word Embeddings
        </button>

      </div>

      <Separator />

      <div className="flex items-center gap-3 p-4">

        <Avatar>
          <AvatarFallback>RB</AvatarFallback>
        </Avatar>

        <div>

          <p className="font-medium">
            Raam
          </p>

          <p className="text-xs text-zinc-400">
            AIML Student
          </p>

        </div>

      </div>

    </aside>
  );
}