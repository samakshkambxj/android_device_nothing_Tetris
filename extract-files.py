#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.file import File
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/nothing/Tetris',
    'hardware/mediatek',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    'vendor.mediatek.hardware.videotelephony@1.0': lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libimsma.so': blob_fixup()
        .replace_needed('libsink.so', 'libsink-mtk.so'),
    'vendor/bin/hw/vendor.noth.hardware.charge-service': blob_fixup()
        .add_needed('libbase_shim.so'),
    'vendor/lib64/hw/audio.primary.mediatek.so': blob_fixup()
        .replace_needed('libalsautils.so', 'libalsautils-v33.so'),
    (
        'vendor/bin/hw/mt6878/android.hardware.graphics.allocator-V2-service-mediatek.mt6878',
        'vendor/lib64/egl/mt6878/libGLES_mali.so',
        'vendor/lib64/hw/mt6878/android.hardware.graphics.allocator-V2-mediatek.so',
        'vendor/lib64/hw/mt6878/android.hardware.graphics.mapper@4.0-impl-mediatek.so',
        'vendor/lib64/hw/mt6878/mapper.mediatek.so',
        'vendor/lib64/libaimemc.so',
        'vendor/lib64/libcodec2_fsr.so',
        'vendor/lib64/libcodec2_vpp_AIMEMC_plugin.so',
        'vendor/lib64/libcodec2_vpp_AISR_plugin.so',
        'vendor/lib64/libmtkcam_grallocutils.so',
        'vendor/lib64/mt6878/libmtkcam_grallocutils.so',
        'vendor/lib64/libmtkcam_grallocutils_aidlv1helper.so',
        'vendor/lib64/vendor.mediatek.hardware.camera.isphal-V1-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V2-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V4-ndk.so',
        'vendor/lib64/vendor.mediatek.hardware.pq_aidl-V7-ndk.so',
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.common-V4-ndk.so', 'android.hardware.graphics.common-V7-ndk.so'),
    (
        'vendor/lib64/libmtkcam_grallocutils.so',
        'vendor/lib64/mt6878/libmtkcam_grallocutils.so',
        'vendor/lib64/libmtkcam_grallocutils_aidlv1helper.so',
        'vendor/lib64/libntcamcore.so',
    ): blob_fixup()
        .replace_needed('android.hardware.graphics.allocator-V1-ndk.so', 'android.hardware.graphics.allocator-V2-ndk.so'),
    (
        'vendor/lib64/mt6878/libdpframework.so',
        'vendor/lib64/libpqsharememory.so',
    ): blob_fixup()
        .replace_needed('vendor.mediatek.hardware.pq_aidl-V2-ndk.so', 'vendor.mediatek.hardware.pq_aidl-V7-ndk.so'),
    'vendor/lib64/hw/hwcomposer.mtk_common.so': blob_fixup()
        .replace_needed('vendor.mediatek.hardware.pq_aidl-V4-ndk.so', 'vendor.mediatek.hardware.pq_aidl-V7-ndk.so'),
    'vendor/lib64/mt6878/libpqconfig.so': blob_fixup()
        .replace_needed('android.hardware.sensors-V2-ndk.so', 'android.hardware.sensors-V3-ndk.so'),
    'vendor/lib64/vendor.mediatek.hardware.bluetooth.audio-V1-ndk.so': blob_fixup()
        .replace_needed('android.hardware.audio.common-V1-ndk.so', 'android.hardware.audio.common-V2-ndk.so'),
    'vendor/lib64/mt6878/libmtkcam_hal_aidl_common.so': blob_fixup()
        .replace_needed('android.hardware.camera.common-V2-ndk.so', 'android.hardware.camera.common-V1-ndk.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'Tetris',
    'nothing',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
