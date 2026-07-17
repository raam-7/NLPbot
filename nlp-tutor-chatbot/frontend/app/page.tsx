import Sidebar from "@/components/sidebar/Sidebar";
import ChatWindow from "@/components/chat/ChatWindow";

export default function HomePage() {
  return (
    <main className="flex h-screen">
      <Sidebar />
      <ChatWindow />
    </main>
  );
}