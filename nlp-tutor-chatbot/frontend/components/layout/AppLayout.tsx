import Sidebar from "@/components/sidebar/Sidebar";
import ChatWindow from "@/components/chat/ChatWindow";

export default function AppLayout() {
  return (
    <div className="flex h-screen bg-zinc-950 text-white">
      <Sidebar />
      <ChatWindow />
    </div>
  );
}