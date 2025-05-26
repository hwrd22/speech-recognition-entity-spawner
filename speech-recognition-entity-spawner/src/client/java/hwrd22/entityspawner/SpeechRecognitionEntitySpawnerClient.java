package hwrd22.entityspawner;

import hwrd22.entityspawner.network.CommandPayload;

import net.fabricmc.api.ClientModInitializer;
import net.minecraft.client.MinecraftClient;
import net.minecraft.network.packet.c2s.common.CustomPayloadC2SPacket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Objects;
import java.util.logging.Level;
import java.util.logging.Logger;

public class SpeechRecognitionEntitySpawnerClient implements ClientModInitializer {
	private static final Logger LOGGER = Logger.getLogger(SpeechRecognitionEntitySpawner.class.getName());

	@Override
	public void onInitializeClient() {
		// This entrypoint is suitable for setting up client-specific logic, such as rendering.
		new Thread(() -> {
			ServerSocket server = null;
			try {
				// Web Socket for the Python script
				server = new ServerSocket(7777);
				System.out.println("Listening for connections on port 7777");
				while (true) {
					Socket client = server.accept();
					BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
					String cmd;

					while ((cmd = in.readLine()) != null) {
						sendCommand(cmd);
					}

					client.close();
				}
			} catch (IOException e) {
				LOGGER.log(Level.SEVERE, "An IOException occurred:", e);
			} finally {
				if (server != null) {
					try {
						server.close();
					} catch (IOException e) {
						LOGGER.log(Level.SEVERE, "An IOException occurred:", e);
					}
				}
			}
		}).start();
	}

	private void sendCommand(String cmd) {
		MinecraftClient client = MinecraftClient.getInstance();
		if (client.player == null)
			return;

		CommandPayload cmdPayload = new CommandPayload(client.player.getUuid(), cmd);
		Objects.requireNonNull(client.getNetworkHandler()).sendPacket(new CustomPayloadC2SPacket(cmdPayload));
	}
}