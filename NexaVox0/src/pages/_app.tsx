import { type AppType } from "next/app";
import Head from "next/head";

import "~/styles/globals.css";
import "@livekit/components-styles";
import "@livekit/components-styles/prefabs";
import { api } from "~/utils/api";

const MyApp: AppType = ({ Component, pageProps }) => {
  return (
    <>
      <Head>
        <title>Nexa Vox</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Component {...pageProps} />
    </>
  );
};

export default api.withTRPC(MyApp);
