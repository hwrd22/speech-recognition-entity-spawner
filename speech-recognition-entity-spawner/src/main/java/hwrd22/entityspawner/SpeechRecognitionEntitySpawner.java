package hwrd22.entityspawner;

import hwrd22.entityspawner.network.CommandPayload;

import net.fabricmc.api.ModInitializer;

import net.fabricmc.fabric.api.networking.v1.PayloadTypeRegistry;
import net.fabricmc.fabric.api.networking.v1.ServerPlayNetworking;
import net.minecraft.entity.EntityType;
import net.minecraft.entity.SpawnReason;
import net.minecraft.entity.mob.MobEntity;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.server.world.ServerWorld;
import net.minecraft.util.math.BlockPos;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Map;
import java.util.HashMap;

public class SpeechRecognitionEntitySpawner implements ModInitializer {
	public static final String MOD_ID = "speech-recognition-entity-spawner";

	// This logger is used to write text to the console and the log file.
	// It is considered best practice to use your mod id as the logger's name.
	// That way, it's clear which mod wrote info, warnings, and errors.
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

	// Create a map to store the mob names and their corresponding EntityType
	private static final Map<String, EntityType<?>> MOB_MAP = new HashMap<>();

	static {
		// Multiple
		MOB_MAP.put("zombie", EntityType.ZOMBIE);
		MOB_MAP.put("skeleton", EntityType.SKELETON);
		MOB_MAP.put("creeper", EntityType.CREEPER);
		MOB_MAP.put("bee", EntityType.BEE);
		MOB_MAP.put("wolf", EntityType.WOLF);
		MOB_MAP.put("polar_bear", EntityType.POLAR_BEAR);
		MOB_MAP.put("spider", EntityType.SPIDER);
		MOB_MAP.put("witch", EntityType.WITCH);
		MOB_MAP.put("silverfish", EntityType.SILVERFISH);
		MOB_MAP.put("phantom", EntityType.PHANTOM);
		MOB_MAP.put("enderman", EntityType.ENDERMAN);
		MOB_MAP.put("pillager", EntityType.PILLAGER);
		MOB_MAP.put("slime", EntityType.SLIME);
		MOB_MAP.put("breeze", EntityType.BREEZE);
		MOB_MAP.put("guardian", EntityType.GUARDIAN);
		MOB_MAP.put("blaze", EntityType.BLAZE);
		MOB_MAP.put("piglin", EntityType.PIGLIN);
		MOB_MAP.put("ghast", EntityType.GHAST);
		MOB_MAP.put("wither_skeleton", EntityType.WITHER_SKELETON);
		MOB_MAP.put("hoglin", EntityType.HOGLIN);
		MOB_MAP.put("magma_cube", EntityType.MAGMA_CUBE);
		MOB_MAP.put("endermite", EntityType.ENDERMITE);
		MOB_MAP.put("shulker", EntityType.SHULKER);

		// Single
		MOB_MAP.put("iron_golem", EntityType.IRON_GOLEM);
		MOB_MAP.put("ravager", EntityType.RAVAGER);
		MOB_MAP.put("piglin_brute", EntityType.PIGLIN_BRUTE);
		MOB_MAP.put("warden", EntityType.WARDEN);
		MOB_MAP.put("ender_dragon", EntityType.ENDER_DRAGON);
		MOB_MAP.put("wither", EntityType.WITHER);
		MOB_MAP.put("tnt", EntityType.TNT);
	}


	@Override
	public void onInitialize() {
		PayloadTypeRegistry.playC2S().register(CommandPayload.ID, CommandPayload.CODEC);  // Register command packet
		ServerPlayNetworking.registerGlobalReceiver(CommandPayload.ID, (payload, context) -> {
			context.server().execute(() -> {
				executeCommand(context.player(), payload.cmd().split(" ")[1]);
			});
		});
	}

	private void executeCommand(ServerPlayerEntity player, String entityToSpawn) {
		int numberToSpawn = (entityToSpawn.equals("warden") || entityToSpawn.equals("ravager") || entityToSpawn.equals("ender_dragon") || entityToSpawn.equals("piglin_brute") || entityToSpawn.equals("wither") || entityToSpawn.equals("iron_golem") || entityToSpawn.equals("tnt")) ? 1 : 5;
			for (int i = 0; i < numberToSpawn; i++) {
				summonEntity(player, entityToSpawn);
			}
	}

	private void summonEntity(ServerPlayerEntity player, String mobString) {
		if (player.isInCreativeMode() || player.isSpectator()) {
			LOGGER.info(String.join(" ", "Command from", player.getNameForScoreboard(), "ignored. Reason: Player is not in Survival or Adventure Mode."));
			return;  // Ignore players in Creative/Spectator
		}
		// Convert string to Entity
		EntityType<?> entityToSpawn = MOB_MAP.get(mobString);
		// Get player's block position for local difficulty
		BlockPos pos = player.getBlockPos();
		// Create entity
		var entity = entityToSpawn.create(player.getWorld(), SpawnReason.EVENT);

		if (entity != null) {
			// Set entity's location to player's
			entity.updatePosition(player.getX(), player.getY(), player.getZ());
			if (entity instanceof MobEntity mob) {
				// Setup mob equipment (If necessary)
				mob.initialize((ServerWorld) player.getWorld(), player.getWorld().getLocalDifficulty(pos), SpawnReason.EVENT, null);
				// Set mob to be hostile towards player that spawned it
				mob.setTarget(player);
			}

			// Spawn entity
			player.getWorld().spawnEntity(entity);
			// Server log
			LOGGER.info(String.join(" ", "Player", player.getNameForScoreboard(), "spawned", mobString.replace('_', ' '), "from voice command"));
		}
	}
}