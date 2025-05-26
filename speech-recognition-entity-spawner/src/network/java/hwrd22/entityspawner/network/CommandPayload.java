package hwrd22.entityspawner.network;

import net.minecraft.network.RegistryByteBuf;
import net.minecraft.network.codec.PacketCodec;
import net.minecraft.network.codec.PacketCodecs;
import net.minecraft.network.packet.CustomPayload;
import net.minecraft.util.Identifier;
import net.minecraft.util.Uuids;

import java.util.UUID;

public record CommandPayload(UUID uuid, String cmd) implements CustomPayload {
    public static final Id<CommandPayload> ID = new Id<>(Identifier.of("speech-recognition-entity-spawner", "player_uuid"));
    public static final PacketCodec<RegistryByteBuf, CommandPayload> CODEC = PacketCodec.tuple(
            Uuids.PACKET_CODEC, CommandPayload::uuid,
            PacketCodecs.STRING, CommandPayload::cmd,
            CommandPayload::new
    );

    @Override
    public Id<? extends CustomPayload> getId() {
        return ID;
    }
}
