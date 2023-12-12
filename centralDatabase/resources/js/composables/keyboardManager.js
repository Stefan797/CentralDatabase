import { ref, onMounted, onUnmounted } from 'vue';

export function usekeyboardManager() {

    const keyboardShortcuts = ref({});

    function handleKeyPress(event) {
        for (const shortcut in keyboardShortcuts.value) {
            const keys = shortcut.split('+');
            const modifiers = keys.slice(0, keys.length - 1);
            const key = keys[keys.length - 1];

            const hasModifiers = modifiers.every(modifier => event[`${modifier}Key`]);
            const isKeyMatch = event.key.toLowerCase() === key.toLowerCase();

            if (hasModifiers && isKeyMatch) {
                keyboardShortcuts.value[shortcut](event);
            }
        }
    }

    function registerShortcut(shortcut, callback) {
        keyboardShortcuts.value[shortcut.toLowerCase()] = callback;
    }

    function unregisterShortcut(shortcut) {
        delete keyboardShortcuts.value[shortcut.toLowerCase()];
    }

    onMounted(() => {
        window.addEventListener('keydown', handleKeyPress);
    });

    onUnmounted(() => {
        window.removeEventListener('keydown', handleKeyPress);
    });

    return {
        registerShortcut,
        unregisterShortcut,
    };
}
