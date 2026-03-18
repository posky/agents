#!/bin/sh

set -e

SCRIPT_DIR=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd -P)
REPO_ROOT=$(CDPATH='' cd -- "$SCRIPT_DIR/.." && pwd -P)
TARGET_PARENT="$REPO_ROOT/codex/skills"
TARGET_DIR="$TARGET_PARENT/conventional-commits"
SOURCE_DIR="$HOME/.codex/skills/conventional-commits"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "오류: source 디렉터리가 없습니다: $SOURCE_DIR" >&2
  exit 1
fi

if [ ! -d "$TARGET_PARENT" ]; then
  echo "오류: target 부모 디렉터리가 없습니다: $TARGET_PARENT" >&2
  exit 1
fi

if [ "$SOURCE_DIR" = "$TARGET_DIR" ]; then
  echo "오류: source와 target 경로가 같습니다." >&2
  exit 1
fi

echo "🧹 기존 디렉토리 삭제: $TARGET_DIR"
rm -rf "$TARGET_DIR"

echo "📦 복사: $SOURCE_DIR -> $TARGET_DIR"
cp -R "$SOURCE_DIR" "$TARGET_DIR"

if [ ! -d "$TARGET_DIR" ]; then
  echo "오류: 복사 후 target 디렉터리를 찾을 수 없습니다: $TARGET_DIR" >&2
  exit 1
fi

echo "✅ 완료"
