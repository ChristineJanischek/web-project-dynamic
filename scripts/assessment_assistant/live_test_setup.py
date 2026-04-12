from __future__ import annotations

from manage_vscode_extensions import (
    detect_vscode_cli,
    get_extensions_for_profile,
    load_manifest,
    resolve_profile,
    install_extensions,
)


def ensure_live_test_extensions(profile_name: str = "live-test") -> tuple[str, int]:
    """Stellt sicher, dass Live-Test-Extensions vor Bewertungsläufen installiert sind.

    Returns:
        Tuple aus aufgeloestem Profilnamen und Anzahl geplanter/installerter Extensions.
    """
    manifest = load_manifest()
    profile = resolve_profile(manifest, profile_name)

    extensions = get_extensions_for_profile(manifest, profile)
    cli_command = detect_vscode_cli(None)
    result = install_extensions(extensions, cli_command, dry_run=False)
    if result != 0:
        raise RuntimeError(
            f"Installation der VS-Code-Extensions fuer Profil '{profile}' fehlgeschlagen (Exit-Code {result})."
        )

    return profile, len(extensions)
