import { useRouter } from 'vue-router';

export function usehandleroutingManager() {
    const router = useRouter();

    function goToPath(path) {
        router.push(path);
    }

    // function openInNewTab(path) {
    //     const routeData = router.resolve({ path });
    //     window.open(routeData.href, '_blank');
    // };

    return {
        goToPath,
    };
}