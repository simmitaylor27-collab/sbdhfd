if search_text in content:
                        content = content.replace(search_text, replace_text)
                        with open(full_path, "w", encoding="utf-8") as f:
                            f.write(content)
                        msg = f"✅ Đã sửa file: {full_path}"
                        print(msg)
                        log_entries.append(msg)
                    else:
                        msg = f"⚠️ Không tìm thấy chuỗi trong: {full_path}"
                        print(msg)
                        log_entries.append(msg)
                except Exception as e:
                    msg = f"❌ Lỗi với file {full_path}: {e}"
                    print(msg)
                    log_entries.append(msg)

    total_modified = sum('✅' in entry for entry in log_entries)
    summary = f"🔧 Tổng số file đã sửa: {total_modified}
fghjg
