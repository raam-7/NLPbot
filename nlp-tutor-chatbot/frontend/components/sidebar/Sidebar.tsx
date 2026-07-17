export default function Sidebar() {
  return (
    <aside className="w-72 border-r p-4 flex flex-col">
      <h1 className="text-2xl font-bold">
        NLP Tutor
      </h1>

      <button className="mt-6 rounded-lg bg-black p-3 text-white hover:bg-gray-800">
        + New Chat
      </button>

      <div className="mt-8 flex-1">
        <p className="text-sm text-gray-500">
          No conversations yet
        </p>
      </div>
    </aside>
  );
}

