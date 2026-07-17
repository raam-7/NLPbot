export default function ChatInput() {
  return (
    <div className="border-t p-4">
      <div className="mx-auto flex max-w-4xl gap-3">
        <input
          type="text"
          placeholder="Ask an NLP question..."
          className="flex-1 rounded-xl border p-3 outline-none focus:ring-2 focus:ring-blue-500"
        />

        <button className="rounded-xl bg-blue-600 px-6 text-white hover:bg-blue-700">
          Send
        </button>
      </div>
    </div>
  );
}