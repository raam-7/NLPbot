type MessageProps = {
  role: "user" | "assistant";
  content: string;
};

export default function Message({ role, content }: MessageProps) {
  const isUser = role === "user";

  return (
    <div
      className={`flex ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      <div
        className={`max-w-2xl rounded-xl p-4 ${
          isUser
            ? "bg-blue-600 text-white"
            : "bg-gray-100 text-black"
        }`}
      >
        {content}
      </div>
    </div>
  );
}