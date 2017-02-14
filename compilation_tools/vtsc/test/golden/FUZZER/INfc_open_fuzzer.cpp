// This file was auto-generated by VTS compiler.

#include <FuzzerInterface.h>
#include <android/hardware/nfc/1.0/INfc.h>

using namespace ::android::hardware::nfc::V1_0;
using namespace ::android::hardware;

namespace android {
namespace vts {

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    static ::android::sp<INfc> nfc = INfc::getService(true);
    if (nfc== nullptr) { return 0; }

    size_t type_size0 = sizeof(sp<::android::hardware::nfc::V1_0::INfcClientCallback>);
    if (size < type_size0) { return 0; }
    size -= type_size0;
    sp<::android::hardware::nfc::V1_0::INfcClientCallback> arg0;
    memcpy(&arg0, data, type_size0);
    data += type_size0;

    nfc->open(arg0);
    return 0;
}

}  // namespace vts
}  // namespace android