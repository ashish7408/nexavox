import React, { useEffect, useState } from "react";
import TextAnimation from "~/components/animation/text";
import Card from "~/components/card";
import Footer from "~/components/footer";
import Loader from "~/components/loader";
import Navbar from "~/components/navbar";
import SplashScreen from "~/components/splashScreen";
import { api } from "~/utils/api";

// Define the type of room object
interface Room {
  name: string;
  slug: string | null;
  createdAt: Date;
  // Add other properties if needed
}

function Profile() {
  const [rooms, setRooms] = useState<Room[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    async function fetchRooms() {
      try {
        const roomsData = await api.rooms.getRoomsByUser.useQuery();
        if (roomsData.error) {
          throw new Error("Failed to fetch rooms");
        }
        setRooms(roomsData.data || []);
      } catch (error) {
        console.error("Error fetching rooms:", error);
      } finally {
        setIsLoading(false);
      }
    }

    fetchRooms();
  }, []);

  if (isLoading) return <SplashScreen />;

  return (
    <>
      <Navbar status={"loading"} session={null} />
      <div className="mt-10 flex flex-col bg-black p-10 text-gray-100 lg:p-20">
        <div className="my-5 flex items-center justify-center">
          <h2 className="text-center text-2xl font-bold text-white">
            Hello!
          </h2>
        </div>

        <div className="flex flex-col items-center justify-center">
          <TextAnimation
            textStyle="text-lg font-bold text-secondary"
            text="Your Rooms"
          />
          {isLoading && <Loader className="flex items-center justify-center" />}
          {rooms.length === 0 && (
            <p className="mt-2 text-xs font-light text-white">
              You haven't started a room yet
            </p>
          )}
          <div className="flex flex-row flex-wrap items-center justify-center">
            {rooms.map((room, index) => {
              return <Card room={room} key={index} />;
            })}
          </div>
        </div>

        <div className="flex flex-col items-center justify-center">
          <TextAnimation
            textStyle="text-lg font-bold text-secondary"
            text="Rooms you are a part of"
          />

          {rooms.length === 0 && (
            <p className="mt-2 text-xs font-light text-white">
              You haven't joined any rooms yet
            </p>
          )}
          <div className="flex flex-row flex-wrap items-center justify-center">
            {rooms.map((room, index) => {
              return <Card room={room} key={index} />;
            })}
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}

export default Profile;
